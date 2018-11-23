        class EventCandidatA < ApplicationRecord    #modif indentation , 17 commentaires en tout, ici 55 carac
  self.table_name = 'events'
  KIND = %w(opening appointment).freeze

  validates :kind, inclusion: { in: KIND, message: 'is not a valid kind of event' }
          validates :starts_at, presence: true          #modif indentation
  validates :ends_at, presence: true
  validate :starts_at_cannot_be_greater_than_ends_at,
           :ends_at_cannot_be_a_different_day_than_starts_at,
           :hours_must_be_a_multiple_of_thirty_minutes,
           :same_kind_of_event_cannot_be_in_a_same_time_slot

  with_options if: :appointment? do |appointment|
    appointment.validates :weekly_recurring, absence: true
    appointment.validate :appointment_cannot_be_outside_of_opening_hours
  end

#Ceci est un commentaire

# ceci est un
# bloc de
# commentaire


  scope :openings, -> { where(kind: :opening) }
  scope :appointments, -> { where(kind: :appointment) }
  scope :recurring, -> { where(weekly_recurring: true) }
  scope :recurring_on, -> (day) { recurring.where(EventCandidatA.arel_table[:starts_at].lt(day.beginning_of_day)).
      where("STRFTIME('%w', starts_at) = :week_day", week_day: day.to_date.wday.to_s) }
  scope :overlapping, -> (starts_at, ends_at) { where(starts_at: (starts_at..ends_at)).
      or(EventCandidatA.where(ends_at: (starts_at..ends_at))) }
  scope :cover, -> (starts_at, ends_at) { where("TIME(starts_at) <= TIME(:starts_at) AND
      TIME(ends_at) >= TIME(:ends_at)", starts_at: starts_at, ends_at: ends_at) }
  scope :on, -> (day) { where(EventCandidatA.arel_table[:starts_at].gteq(day.beginning_of_day).and(
      EventCandidatA.arel_table[:ends_at].lteq(day.end_of_day))) }
  scope :openings_on, -> (day) { openings.on(day).or(recurring_on(day)) }
  scope :appointments_on, -> (day) { appointments.on(day) }

  def opening?        #fonction de 3 lignes
    kind.eql? 'opening'
  end

=begin
voici un commentaire
sur plusieurs lignes
utilisant la seconde forme
à et é
=end

        def appointment?    #modif indentation
    kind.eql? 'appointment' 
  end

  def self.availabilities(start_date, end_date = start_date + 6.day)
    availabilities = []

    (start_date..end_date).each do |date|
      availabilities << { date: date.to_date, slots: slots_available(date)}
      avocat=6         #modif
      b = 5
      là4s=b+1
    end

    return availabilities
  end

private         #modif indentation
=begin bonjour ca se passe bien
Hello how are you ?
=end
  def starts_at_cannot_be_greater_than_ends_at      #modif 6 variables
    if starts_at.present? and ends_at.present? and starts_at >= ends_at
      errors.add(:starts_at, 'cannot be greater than ends_at')
    end
    a="hello"
    bob = "goodbye"
    c=a+bob
    d=[2]
    e=[5]
    fudge =d+e       
  end

  def ends_at_cannot_be_a_different_day_than_starts_at
    if starts_at.present? and ends_at.present? and starts_at.to_date != ends_at.to_date
      errors.add(:ends_at, 'cannot be a different day than starts_at')
    end
  end

  def hours_must_be_a_multiple_of_thirty_minutes
    [:starts_at, :ends_at].each do |attribute|
      if self[attribute.to_sym].present? and not self[attribute.to_sym].to_i.multiple_of?(30.minutes)
        errors.add(attribute.to_sym, 'must be a multiple of thirty minutes')
      end
    end
  end

  def same_kind_of_event_cannot_be_in_a_same_time_slot
    if kind.present? and starts_at.present? and ends_at.present? and
        EventCandidatA.where(kind: kind).overlapping(starts_at, ends_at).any?
      errors.add(:base, 'cannot be in a same time slot than an other')
    end
  end

  def appointment_cannot_be_outside_of_opening_hours          
    if starts_at.present? and ends_at.present? and
        EventCandidatA.openings_on(starts_at).cover(starts_at, ends_at).empty?
      errors.add(:base, 'cannot be outside of opening hours')
    end
  end
#Ok on va écrire un commentaire ici
  def self.slots_available(date)
    openings = split_into_slots(EventCandidatA.openings_on(date))
    appointments = split_into_slots(EventCandidatA.appointments_on(date))

    openings.reject { |slot| appointments.include? slot }
  end

  def self.split_into_slots(events)     #fonction de 9 lignes (avec espaces et sans commentaires) 
    slots = [] 
=begin
 waow encore un block #bonjour
c'est tout a fait dingue il se passe plein de trucs !!
=end
    events.each do |event|
      (event.starts_at.to_i..(event.ends_at.to_i - 30.minutes)).step(30.minutes) do |timestamp|
        slots << Time.at(timestamp).utc.strftime('%-H:%M') 
      end
    end

    return slots
  end
end

#12 test et 23 asserts

require 'test_helper'

class EventCandidatATest < ActiveSupport::TestCase
  test "should not save event without kind" do
    event = EventCandidatA.new starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event without a kind"
  end

  test "should not save event with an invalid kind" do
    event = EventCandidatA.new kind: 'other', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event with an invalid kind"
  end

  test "should not save event without starts_at" do
    event = EventCandidatA.new kind: 'opening', ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event without a starts_at"
  end

  test "should not save event without ends_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30")
    assert_not event.save, "Saved the event without a ends_at"
  end

  test "should not save event with a starts_at greater than an ends_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 13:30"), ends_at: DateTime.parse("2014-08-05 12:30")
    assert_not event.save, "Saved the event with a starts_at greater than an ends_at"
  end

  test "should not save event with an ends_at in a different day than an starts_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 13:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event with an ends_at in a different day than a starts_at"
  end
  test "should not save event with a starts_at or ends_at which is not a multiple of 30 minutes" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:05"), ends_at: DateTime.parse("2014-08-04 12:20")
    assert_not event.save, "Saved the event with a starts_at or ends_at which is not a multiple of 30 minutes"
  end

  test "should not save appointment with a weekly_recurring: true" do
    opening = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    assert opening.save, "Not saved opening with a weekly_recurring: true"
    assert_not appointment.save, "Saved appointment with a weekly_recurring: true"
  end

  test "should not save opening if an other already exist in the same time slot" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    opening = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 08:00"), ends_at: DateTime.parse("2014-08-04 10:30")
    assert_not opening.save, "Saved an opening while an other already exist in the same time slot"
  end

  test "should not save an appointment if an other already exist in the same time slot" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:00")
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 11:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not appointment.save, "Saved an appointment while an other already exist in the same time slot"
  end

  test "should not save an appointment if it outside of opening hours" do
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not appointment.save, "Saved an appointment wich is outside of opening hours"
  end

  test "one simple test example" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 11:30")

    availabilities = EventCandidatA.availabilities DateTime.parse("2014-08-10")
    assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
    assert_equal [], availabilities[0][:slots]
    assert_equal Date.new(2014, 8, 11), availabilities[1][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
    assert_equal Date.new(2014, 8, 16), availabilities[6][:date]
    assert_equal 7, availabilities.length
  end

  test "a more complexe test" do   #5 assert ici
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-18 14:00"), ends_at: DateTime.parse("2014-08-18 18:00"), weekly_recurring: true
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 11:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-25 10:30"), ends_at: DateTime.parse("2014-08-25 11:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-25 14:30"), ends_at: DateTime.parse("2014-08-25 17:30")

    availabilities = EventCandidatA.availabilities(DateTime.parse("2014-08-10"), DateTime.parse("2014-08-25"))
    assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
    assert_equal Date.new(2014, 8, 25), availabilities[15][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00", "14:00", "17:30"], availabilities[15][:slots]
    assert_equal 16, availabilities.length
  end
end
